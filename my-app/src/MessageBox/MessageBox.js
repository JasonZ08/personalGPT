import React from "react";
import './MessageBox.css'
import { Container } from "react-bootstrap";

const MessageBox = (props) => {
    const { message, user } = props;

    return (
        user ?
        <Container className="d-flex justify-content-end py-3">
            <div className="chatMessage bg-info p-sm-3 m-sm-2">
                {message}
            </div>
        </Container> :
        <Container className="d-flex py-3">
            <div className="chatMessage bg-danger p-sm-3 m-sm-2">
                {message}
            </div>
        </Container>
    )
}

export default MessageBox