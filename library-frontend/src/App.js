import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import './App.css';
import { useEffect, useState } from 'react';

function App() {

  const [books, setBooks] = useState([])
  const [shelf, setShelf] = useState([])
  const [catalogue, setCatalogue] = useState([])

  useEffect(() => {
    async function fetchBooks() {
      await fetch('http://127.0.0.1:8000/api/v1/books/')
        .then((response) => response.json())
        .then((responseJSON) => {
          console.log(responseJSON)
          setBooks(responseJSON)
        })
    }
    async function fetchShelves() {
      await fetch('http://127.0.0.1:8000/api/v1/shelves/')
        .then((response) => response.json())
        .then((responseJSON) => {
          console.log(responseJSON)
          setShelf(responseJSON)
        })
    }
    async function fetchCatalogues() {
      await fetch('http://127.0.0.1:8000/api/v1/catalogues/')
        .then((response) => response.json())
        .then((responseJSON) => {
          console.log(responseJSON)
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
              <Button variant="primary">Go somewhere</Button>
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
              <Button variant="primary">Go somewhere</Button>
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
              <Button variant="primary">Go somewhere</Button>
            </Card.Body>
          </Card>
        )
      })}
    </div>
  );
}

export default App;
