import React from "react";
import Stack from 'react-bootstrap/Stack';
import './Home.css'
import MessageBox from '../MessageBox/MessageBox';

const Home = (props) => {
    const { messageList } = props

    return (
        <div>
            <Stack className="Messages">
                {messageList.map((value, i) => {
                    if (value !== '') {
                        return (<MessageBox key = {i} message={value.message} user={value.user} />)
                    }
                    else {
                        return <></>
                    }
                })}
            </Stack>
        </div>
    )
}

export default Home