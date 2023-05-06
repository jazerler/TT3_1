import Form from "react-bootstrap/Form";
import Dropdown from "react-bootstrap/esm/Dropdown";
import { useState } from "react";
// import DatePicker from 'react-datepicker';


const CURRENCIES = ["CNY",
"HKD",
"IDR",
"INR",
"JPY",
"KHR",
"KRW",
"SGD",
"TWD",
"VND"]



const Newclaim = () => {
    const [currency, setCurrency] = useState('')
    const [firstName, setFirstName] = useState('')
    const [lastName, setLastName] = useState('')
    const [date, setDate] = useState('')
    const [claimAmount, setClaimAmount] = useState('')
    const [claimPurpose, setClaimPurpose] = useState('')



    return (
        <div>
            <header>
                <h1>Add new claim</h1>
            </header>
            <form>
                
                First name: 
                <input type="text"></input>
                <br />

                Last name:
                <input type="text"></input>
                <br />

                Purpose for claim:
                <input type="text"></input>
                <br />

                Date:
                <input type="date" onChange={x => setDate(x)}></input>
                <br />
                
                Currency:
                <Form.Select onChange={(v) => setCurrency(v)}>
                    {CURRENCIES.map((variant) => (<option value={variant}>{variant}</option>))}
                </Form.Select>


                Claim amount: 
                <input  type="number" onChange={c => setClaimAmount(c)}></input>
                <br />


            </form>

            <button>Submit new claim</button>
            <button>Cancel</button>


        </div>
    )
  }



export default Newclaim;