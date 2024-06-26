import Home from './pages/Home/Home'
import './App.css'
import SignUp from './pages/signup/SignUp'
import Login from './pages/login/Login'
import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import Dashboard from './pages/Dashboard/Dashboard';
import Report from './pages/report/Report'
import Scans from './pages/scans/Scans'
import Notfound from './components/Notfound';
function App() {
  
  return (
    <>
      <Router>
        <Routes>
          <Route path='/' element={<Home/>}/>
          <Route path='/signup' element={<SignUp/>}/>
          <Route path='/login' element={<Login/>}/>
          <Route path='/dashboard' element={<Dashboard  />}/>
          <Route path='/scans/*' element={<Scans />}/>
          <Route path='/report' element={<Report/>}/>
          <Route path='*' element={<Notfound/>}/>
        </Routes>
      </Router>
    </>
  )
}

export default App
