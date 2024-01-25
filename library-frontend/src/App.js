import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import './App.css';
import { useEffect, useState } from 'react';

function App() {

  const [books, setBooks] = useState([])

  useEffect(() => {
    async function fetchData() {
      await fetch('http://127.0.0.1:8000/api/v1/books/')
        .then((response) => response.json())
        .then((responseJSON) => {
          console.log(responseJSON)
          setBooks(responseJSON)
        })
    }
    fetchData()
  }, [])

  return (
    <div className="App">
      <h1>Library</h1>
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
    </div>
  );
}

export default App;
