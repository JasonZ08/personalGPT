import React, { useState } from 'react'
import Header from './Navbar/Navbar'
import TextBox from './TextBox/TextBox'
import Home from './Home/Home'
import 'bootstrap/dist/css/bootstrap.min.css'

function App() {

  const [value, setValue] = useState("")
  const [messageList, setMessageList] = useState([""])
  const [myData, setMyData] = useState("") 
  

  const onFormSubmit = async () => {
    
    setMessageList((messageList) => [...messageList, {message: value, user:true}])
    
    const response = await fetch("/chat", {
          method: 'POST',
          headers: { "Content-Type": "application/json"},
          body: JSON.stringify(value)
    })
    const data = await response.json()


    setMyData(data)
    console.log(myData)

    const answer = data.response

    setMessageList((messageList) => [...messageList, {message: answer, user:false}])

  }

  return (
    <div>
      <Header />
      <Home messageList={messageList}/>
      <TextBox setMessageInput = {setValue} submitMessage = {onFormSubmit}/>
    </div>
  );
}

export default App;
