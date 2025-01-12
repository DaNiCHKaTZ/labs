import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { Provider } from 'react-redux';
import PostForm from './components/PostForm.js';
import PostList from './components/PostList.js';
import PostDetail from './components/PostDetail.js';
import store from './store';
import './App.css';

function App() {
  return (
    <Provider store={store}>
      <Router>
        <div className="App">
          <nav>
            <Link to="/">Список постов</Link>
            <Link to="/add">Добавить пост</Link>
          </nav>
          <Routes>
            <Route path="/" element={<PostList />} />
            <Route path="/add" element={<PostForm />} />
            <Route path="/post/:id" element={<PostDetail />} />
          </Routes>
        </div>
      </Router>
    </Provider>
  );
}

export default App;
