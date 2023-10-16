import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';

function Header() {
  return (
    <Navbar bg="dark" data-bs-theme="dark" className='py-3'>
        <Container>
          <Navbar.Brand href="#home">
            <h3>PersonalGPT</h3>
          </Navbar.Brand>
        </Container>
      </Navbar>
  );
}

export default Header;