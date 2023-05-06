

const Claim = ({claim}) => {

    return (
        <div className = 'claim'>
            <h3 style={{textAlign:'left'}}>PROJECT ID {claim.projectID}</h3>
            <p style={{textAlign:'left'}}> {`Status: ${claim.status} |
            Claim ID: ${claim.claimsID} | Currency: ${claim.currency}`}
            </p>
            <div button
                    type="button"
                    className="btn btn-secondary btn-lg modify-modal"
                    style={{ height: 50, width: 200 }}
                >
                    Modify
                </div>
    
        </div>
    )
  }

export default Claim