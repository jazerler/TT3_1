import { useEffect, useState } from "react";
import Claims from "../components/Claims.js";

function Dashboard(props) {
    const [] = useState()

    const handleRetriveClaim = async (event) => {
        event.preventDefault();

        let formData = new FormData();
        formData.append('EmployeeID', props.user)
    
        try {
          const response = await fetch(
            "http://127.0.0.1:5000/retrieveClaim",
            {
              method: 'POST',
              headers: {
                'content-type': 'multipart/form-data'
              },
              body: formData
            }
          );
        } catch (err) {
            console.log("Error fetching")
        }
    }

    useEffect(() => {
        handleRetriveClaim()
    }, [])

    return (
        <div>
            <header>
                <h1>Welcome, Username</h1>
                <h2 style={{textAlign:'left'}}>Your claim records:</h2>
            </header>
            
            <Claims />


        </div>
        
    )
}

export { Dashboard };