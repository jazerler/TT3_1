

const Claim = ({claim}) => {

    return (
        <div className = 'claim'>
            <h3 style={{textAlign:'left'}}>PROJECT ID {claim.ProjectId}</h3>
            <p style={{textAlign:'left'}}> {`Status: ${claim.status} |
            Claim ID: ${claim.claimID} | Currency: ${claim.currencyID}`}
            </p>
    
        </div>
    )
  }

export default Claim