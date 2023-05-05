import { useEffect, useState } from "react";
import Claims from "../components/Claims.js";

function Dashboard(props) {

    return (
        <div>
            <header>
                <h1>Welcome, {props.user}</h1>
                <h2 style={{textAlign:'left'}}>Your claim records:</h2>
            </header>
            
            <Claims user={props.user}/>

            <div button
                type="button"
                className="btn btn-secondary btn-lg new-claim-modal"
                style={{ height: 50, width: 200 }}>
                New Claim
            </div>

        </div>
        
    )
}

export { Dashboard };