import { useState } from "react";
import Claims from "../components/Claims.js";

function Dashboard(props) {
    const [] = useState()

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