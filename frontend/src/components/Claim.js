

const Claim = ({claim}) => {

    return (
        <div className = 'claim'>
            <h3 style={{textAlign:'left'}}>PROJECT ID {claim.ProjectId}</h3>
            <p style={{textAlign:'left'}}> {`Status: ${claim.status} |
            Claim ID: ${claim.claimID} | Currency: ${claim.currencyID}`}
            </p>
            <div button
                type="button"
                className="btn btn-secondary btn-lg modify-modal"
                style={{ height: 50, width: 200 }}>
                Edit Claim
            </div>
    
        </div>
    )
  }

export default Claim