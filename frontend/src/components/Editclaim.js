const Editclaim = () => {

    return (
        <div>
            <header>Add new claim</header>
            <form>First Name:  
                <input type="text"></input>
                <br />

                Last name:
                <input type="text"></input>

                Purpose for claim:
                <input type="text"></input>

                Claim amount:

                <div class="dropdown">
                    <button class="dropbtn">Dropdown</button>
                    <div class="dropdown-content">
                        <li>SGD</li>
                        <li>USD</li>
                        <li></li>
                    </div>
                </div>



            </form>


        </div>
    )
  }



export default Editclaim;