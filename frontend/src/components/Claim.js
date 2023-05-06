

const Claim = ({claim}) => {

    return (
        <div className = 'claim'>
            <h3 style={{textAlign:'left'}}>PROJECT ID {claim.projectID}</h3>
            <p style={{textAlign:'left'}}> {`Status: ${claim.status} |
            Claim ID: ${claim.claimsID} | Currency: ${claim.currency}`}
            </p>
    
        </div>
    )
  }

export default Claim