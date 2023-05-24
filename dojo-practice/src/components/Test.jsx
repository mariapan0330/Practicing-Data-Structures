// build a text with a border
// ask the user for an input and whatever they input, put it in the box
// have a button that hides the component

import React, { useState } from 'react'

export default function Test() {
    const [val, setVal] = useState("This is a box");
    const [hideBox, setHideBox] = useState(false);

    console.log(hideBox)

    const formHandler = (e) => {
        setVal(e.target.value)
    }

    const handleHideBox = () => {
        setHideBox(p => {
            return !p
        })

        // if (hideBox == true){
        //     setHideBox(false)
        // } else{
        //     setHideBox(true)
        // }
    }

    return (
        <div>
            <input name='inp' type="text" onChange={formHandler}></input>
            {
                hideBox ?
                <>
                <div></div>
                <button onClick={handleHideBox}>Show the box</button>
                </>
                :
                <>
                <div style={{borderStyle: 'solid'}}>
                    {val}
                </div>
                <button onClick={handleHideBox}>Hide the box</button>
                </>
            }
        </div>
    )
}
