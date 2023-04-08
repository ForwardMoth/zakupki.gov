import { Routes, Route, BrowserRouter } from "react-router-dom";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
// import Parser from "../pages/Parser";
import logo from './logo.jpg';

import MainPage from '../pages/MainPage';
import Notice from '../pages/Notice';
import Contracts from '../pages/Contracts';
import Statistics from "../pages/Statistics";

const Header = () => {
  return (
    <>
    <Navbar fixed='top' bg="light" expand="md">
      <Container>
        <Navbar.Brand href="/">
                  <img 
                    src={logo}
                    height="30"
                    width="30"
                    className="d-inline-block align-top"
                    alt="Logo"
                />
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/notice">Даннные о извещениях</Nav.Link>
            <Nav.Link href="/contracts">Данные о контрактах</Nav.Link>
            {/* <Nav.Link href="/parser">Загрузка данных</Nav.Link> */}
            <Nav.Link href="/statistics">Статистика данных</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<MainPage />} />
        <Route exact path="/notice" element={<Notice />} />
        <Route exact path="/contracts" element={<Contracts />} />
        {/* <Route exact path="/parser" element={<Parser />} /> */}
        <Route exact path="/statistics" element={<Statistics />} />
      </Routes>
    </BrowserRouter>
    </>
  );
}

export default Header;

