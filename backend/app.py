from flask import Flask, request, jsonify
import threading
import uuid
from db import save_scan_results, get_scan_results, save_processed_results, get_processed_results
from scan import run_nmap_scan, run_whatweb_scan, run_wpscan
from filter import parse_nmap_results, filter_whatweb_scan, parse_wp_results, find_vulnerabilities, find_users, find_themes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def active_scan(target, scan_id):
    def run_scans():
        nmap_results = run_nmap_scan(target)
        whatweb_results = run_whatweb_scan(target)
        wpscan_results = run_wpscan(target)

        scan_data = {
            'nmap_raw': nmap_results,
            'whatweb_raw': whatweb_results,
            'wpscan_raw': wpscan_results
        }
        save_scan_results(scan_id, scan_data)
        processed_data = {
            'nmap': parse_nmap_results(nmap_results),
            'whatweb': filter_whatweb_scan(whatweb_results),
            'general': parse_wp_results(wpscan_results),
            'vulnerabilities': find_vulnerabilities(wpscan_results),
            'users': find_users(wpscan_results)
        }
        save_processed_results(scan_id, processed_data)
    thread = threading.Thread(target=run_scans)
    thread.start()

@app.route('/start-active-scan', methods=['POST'])
def start_active_scan():
    data = request.json
    target = data['target']
    scan_id = str(uuid.uuid4())
    active_scan(target, scan_id)
    return jsonify({'scan_id': scan_id, 'status': 'pending'}), 202

@app.route('/scan-results/<scan_id>', methods=['GET'])
def scan_results(scan_id):
    scan_data = get_scan_results(scan_id)
    if not scan_data:
        return jsonify({'error': 'Scan not found'}), 404
    processed_data = get_processed_results(scan_id)
    if not processed_data:
        return jsonify({'error': 'Processed scan data not found'}), 404
        
    nmap_raw = scan_data.get('nmap_raw', '')
    whatweb_raw = scan_data.get('whatweb_raw', '')
    wpscan_raw = scan_data.get('wpscan_raw', '')

    parsed_nmap_results = parse_nmap_results(nmap_raw)
    filtered_whatweb_results = filter_whatweb_scan(whatweb_raw)
    parsed_wpscan_general = parse_wp_results(wpscan_raw)
    wpscan_plugins = find_vulnerabilities(wpscan_raw)
    wpscan_users = find_users(wpscan_raw)
    wpscan_themes = find_themes(wpscan_raw)

    result = {
        'nmap': parsed_nmap_results,
        'whatweb': filtered_whatweb_results,
        'general': parsed_wpscan_general,
        'plugins': wpscan_plugins,
        'themes' : wpscan_themes,
        'users': wpscan_users
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)