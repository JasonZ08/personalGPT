import Form from 'react-bootstrap/Form';
import { Button, Col, Container, Row } from 'react-bootstrap'

/*try to make row/col flex boxes so its responsive*/

const TextBox = (props) => {
    const { setMessageInput, submitMessage } = props

    return (
        <>
            <Container fluid className="bg-secondary form py-4">
                <Form className="py-4">
                    <Row className='d-flex justify-content-center align-items-center'>
                        <Col xs={5}>
                            <Form.Control
                            type="text"
                            placeholder='Send a message'
                            className='mr-sm-2 py-2'
                            onChange={(e) => {setMessageInput(e.target.value)}}
                            />
                        </Col>
                        <Col xs="auto">
                            <Button variant="dark" onClick={submitMessage} type="reset">Submit</Button>
                        </Col>
                    </Row>
                </Form>
            </Container>
        </>
    )
}

export default TextBox