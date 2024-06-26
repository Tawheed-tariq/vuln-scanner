import ParticlesBg from 'particles-bg' //using particles-bg because react-particles-js is not working

export default function FormLayout({children}){
    let numberOfParticles = 150

    if(window.innerWidth < 786){
        numberOfParticles = 50
    }else if(window.innerWidth < 1024){
        numberOfParticles = 100
    }

    return(
        <div className={`flex formLayout justify-center items-center h-[100vh]`}>
            <div className={`flex flex-col w-full justify-center items-center max-w-[350px] ss:max-w-[500px] sm:max-w-[700px] md:max-w-[900px] backdrop-blur-sm bg-secondary-50 px-[20px] md:px-[40px] pt-[30px] pb-[50px] rounded-3xl`}>
                <h1 className="text-[25px] sm:text-[30px] md:text-[40px] text-text font-bold">WP-Scanner</h1>

                <p className={`text-[12px] sm:text-[16px] md:text-[20px] text-text mt-[10px]`}>
                    Sign up to access our WordPress Scanner, a powerful tool 
                    for detecting website vulnerabilities. Easily identify and 
                    mitigate security risks to fortify your online presence.
                </p>

                <hr className={`w-full border-text mt-[10px] mb-[20px] md:mb-[40px]`} />
                <div>
                    {children}
                </div>
            </div>
            <ParticlesBg
                type="cobweb"
                num={numberOfParticles}
                bg={true} 
                size={10} 
                speed={3}
            />
        </div>
    )
}