import React, { useState, useEffect } from "react";
import Navbar from "./navbar";
import Footer from "./footer";
import AdItemRokomari from "./rokomari_ad_item";
import SideHumayun from "./humayunSide";

function RokomariPage() {
  const [books, setBooks] = useState([]);
  const [titleSearchQuery, setTitleSearchQuery] = useState("");
  const [authorSearchQuery, setAuthorSearchQuery] = useState("");
  const [filteredBooks, setFilteredBooks] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8091/app/books_shelf")
      .then((response) => response.json())
      .then((data) => {
        setBooks(data.books);
        setFilteredBooks(data.books);
      });
  }, []);

  const handleTitleSearch = () => {
    const filtered = books.filter((book) =>
      book.title.toLowerCase().includes(titleSearchQuery.toLowerCase())
    );
    setFilteredBooks(filtered);
  };

  const handleAuthorSearch = () => {
    const filtered = books.filter((book) =>
      book.author.toLowerCase().includes(authorSearchQuery.toLowerCase())
    );
    setFilteredBooks(filtered);
  };

  const handleTitleInputChange = (e) => {
    setTitleSearchQuery(e.target.value);
  };

  const handleAuthorInputChange = (e) => {
    setAuthorSearchQuery(e.target.value);
  };

  const handleClear = () => {
    setTitleSearchQuery("");
    setAuthorSearchQuery("");
    setFilteredBooks(books);
  };

  return (
    <>
      <Navbar />
      <div className="container bg-light" style={{ marginTop: "80px" }}>
        <div className="row">
          <div className="col-3 border-end border-2">
            {<SideHumayun />}
          </div>
          <div className="col-9">
            <div className="mb-3">
              <input
                type="text"
                className="form-control"
                placeholder="Search by title"
                value={titleSearchQuery}
                onChange={handleTitleInputChange}
              />
              <button className="btnbook me-2" onClick={handleTitleSearch}>
                Search by Title
              </button>
              </div>
              <div className="mb-3">
              <input
                type="text"
                className="form-control"
                placeholder="Search by author"
                value={authorSearchQuery}
                onChange={handleAuthorInputChange}
              />
              <button className="btnbook" onClick={handleAuthorSearch}>
                Search by Author
              </button>
              <button className="rightbtn btn btn-danger" onClick={handleClear}>
                Clear
              </button>
            
            </div>
            {filteredBooks.map((book) => (
              <AdItemRokomari ad={book} key={book.id} />
            ))}
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
}

export default RokomariPage;
