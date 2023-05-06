import React from 'react';
import Claim from '../components/Claim.js';
import { useEffect, useState } from 'react';

const claims = [
  {
    "username": "John Doe",
    "ProjectId": 123,
    "status": "Pending",
    "claimID": 123,
    "currencyID": "SGD"
  },

  {
    "username": "John Doe",
    "ProjectId": 124,
    "status": "Accepted",
    "claimID": 124,
    "currencyID": "SGD"
  },

  {
    "username": "Jane Doe",
    "ProjectId": 125,
    "status": "Rejected",
    "claimID": 125,
    "currencyID": "AUD"
  }
]

const Claims = (props) => {

  const [claimsList, setClaims] = useState(claims)

  const handleRetriveClaim = async (event) => {
    
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
      ).then((res) => {
        return res.json
      });

      console.log(response) // set claims to retrieved
      
    } catch (err) {
        console.log("Error fetching")
    }
  }

  useEffect(() => {
      handleRetriveClaim()
  }, [])

  return (
      <>
        {claims.map((claim)=> (
            <Claim key = {claim.ProjectId} claim = {claim} /> 
        ))}
      </>
  )
}

  export default Claims