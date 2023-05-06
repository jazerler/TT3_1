import { useState } from "react";
import Claims from "../components/Claims.js";
import Newclaim from "../components/Newclaim.js";
import Modal  from "react-bootstrap/Modal";

function Dashboard(props) {
    const [showModal, setShowModal] = useState(false)

    return (
        <div className="BackgroundJewel">
            <header>
                <h1 style={{color:"black"}}>Welcome, {props.user}</h1>
                <h2 style={{textAlign:'left'}}>Your claim records:</h2>
            </header>

            <Claims user={props.user}/>

            <div button type="button" className="btn btn-secondary btn-lg new-claim-modal" 
                data-bs-toggle="modal" data-bs-target="#exampleModal"
                style={{ height: 50, width: 200 }}
                onClick={() => setShowModal(!showModal)}>
                New Claim
            </div>
{/* 
            <Popup trigger={<button
                type="button"
                className="btn btn-secondary btn-lg new-claim-modal"
                style={{ height: 50, width: 200 }}>
                New Claim </button>} position="center">
                <div>Popup content here !!</div>
            </Popup> */}



        </div>
        
    )
}

export { Dashboard };