import React, { useState } from 'react'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import 'bootstrap/dist/css/bootstrap.min.css'

function App() {

  const [value, setValue] = useState("")

  const onFormSubmit = () => {
    fetch("/chat", {
      method: 'POST',
      headers: { "Content-Type": "application/json"},
      body: JSON.stringify(value)
    }).then(() => {
      console.log(JSON.stringify({"Message": value}))
      console.log("hi")
    })
  }

  return (
    <div>
      Hello World!
      <Form onSubmit={onFormSubmit}>
        <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
            <Form.Label>Message</Form.Label>
            <Form.Control onChange={(e) => setValue(e.target.value)} placeholder="Your Message" />
        </Form.Group>
        <Button variant='primary' onClick={onFormSubmit}>Submit</Button>
      </Form>
      {value}
    </div>
  );
}

export default App;
