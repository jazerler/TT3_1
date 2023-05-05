import React from 'react';
import Claim from '../components/Claim.js';



const claims = [
    {
      "username": "John Doe",
      "projectID": 123,
      "status": "Pending",
      "claimsID": 123,
      "currency": "SGD"
    },
  
    {
      "username": "John Poe",
      "projectID": 124,
      "status": "Accepted",
      "claimsID": 124,
      "currency": "SGD"
    },
  
    {
      "username": "Jane Doe",
      "projectID": 125,
      "status": "Rejected",
      "claimsID": 125,
      "currency": "AUD"
    }
  ]

  const Claims = () => {

    return (
        <>
        
            {claims.map((claim)=> (
                <Claim key = {claim.projectID} claim = {claim} /> 
            ))}
        
        </>
    )
  }

  export default Claims