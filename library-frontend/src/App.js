import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Card from 'react-bootstrap/Card';
import './App.css';
import { useEffect, useState } from 'react';

export const addBook = async (bookName, price, space) => {
  fetch('http://127.0.0.1:8000/api/v1/books/', {
    method: "POST",
    headers: {
      'Content-Type': "application/json"
    },
    data: {
      name: bookName,
      price: price,
      space_in_cm: space
    }
  })
    .then((res) => {
      console.log(res.json())
      window.location.href = '../'
  })
}

function App() {

  const [books, setBooks] = useState([])
  const [shelf, setShelf] = useState([])
  const [catalogue, setCatalogue] = useState([])

  useEffect(() => {
    async function fetchBooks() {
      await fetch('http://127.0.0.1:8000/api/v1/books/')
        .then((response) => response.json())
        .then((responseJSON) => {
          setBooks(responseJSON)
        })
    }
    async function fetchShelves() {
      await fetch('http://127.0.0.1:8000/api/v1/shelves/')
        .then((response) => response.json())
        .then((responseJSON) => {
          setShelf(responseJSON)
        })
    }
    async function fetchCatalogues() {
      await fetch('http://127.0.0.1:8000/api/v1/catalogues/')
        .then((response) => response.json())
        .then((responseJSON) => {
          setCatalogue(responseJSON)
        })
    }
    fetchBooks()
    fetchShelves()
    fetchCatalogues()
  }, [])

  return (
    <div className="App">
      <h1>Library</h1>
      <h2>Books</h2>
      {books.map((book) => {
        return (
          <Card style={{ width: '18rem' }}>
            <Card.Body>
              <Card.Title>Name: {book.name}</Card.Title>
              <Card.Text>
                Price: {book.price}
              </Card.Text>
            </Card.Body>
          </Card>
        )
      })}
      <h2>Shelves</h2>
      {shelf.map((s) => {
        return (
          <Card style={{ width: '18rem' }}>
            <Card.Body>
              <Card.Title>ID: {s.id}</Card.Title>
              <Card.Text>
                Space(in cm): {s.space_in_cm}
              </Card.Text>
            </Card.Body>
          </Card>
        )
      })}
      <h2>Catalogue</h2>
      {catalogue.map((c) => {
        return (
          <Card style={{ width: '18rem' }}>
            <Card.Body>
              <Card.Title>ID: {c.id}</Card.Title>
              <Card.Text>
                Book ID: {c.book}
              </Card.Text>
              <Card.Text>
                Shelf ID: {c.shelf}
              </Card.Text>
            </Card.Body>
          </Card>
        )
      })}
      <Form border='dark'>
        <Form.Group className="mb-3" controlId="addShelf">
          <Form.Label>Add shelf space(in cm)</Form.Label>
          <Form.Control type="text" placeholder="Enter space in cm" />
        </Form.Group>
        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
      <Form>
        <Form.Group className="mb-3" controlId="addBookName">
          <Form.Label>Name of Book</Form.Label>
          <Form.Control type="text" placeholder="Enter name of Book" id='bookName' />
        </Form.Group>
        <Form.Group className="mb-3" controlId="addBookPrice">
          <Form.Label>Price of Book</Form.Label>
          <Form.Control type="number" placeholder="Enter price of Book" id='bookPrice' />
        </Form.Group>
        <Form.Group className="mb-3" controlId="addBookSpace">
          <Form.Label>Space(in cm)</Form.Label>
          <Form.Control type="number" placeholder="Enter space of Book(in cm)" id='bookSpace' />
        </Form.Group>
        <Button variant="primary" type="submit" onClick={() => {
          addBook(document.getElementById('bookName'), document.getElementById('bookPrice'), document.getElementById('bookSpace'))
        }}>
          Submit
        </Button>
      </Form>
    </div>
  );
}

export default App;
