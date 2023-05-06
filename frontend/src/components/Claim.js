

const Claim = ({claim}) => {

    return (
        <div className = 'claim'>
            <h3>PROJECT ID {claim.projectID}</h3>
            <p> {`Status: ${claim.status} |
            Claim ID: ${claim.claimsID} | Currency: ${claim.currency}`}
            </p>
    
        </div>
    )
  }

export default Claim