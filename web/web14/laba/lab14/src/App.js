import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import PostForm from './components/PostForm.js';
import PostList from './components/PostList.js';
import PostDetail from './components/PostDetail.js';
import postStore from './stores/PostStore.js';
import { createPost, deletePost } from './actions/PostAction.js';
import './App.css';

function App() {
  const [posts, setPosts] = useState(postStore.getAllPosts());

  useEffect(() => {
    postStore.on('change', handleStoreChange);
    return () => postStore.removeListener('change', handleStoreChange);
  }, []);

  const handleStoreChange = () => {
    setPosts(postStore.getAllPosts());
  };

  return (
    <Router>
      <div className="App">
        <nav>
          <Link to="/">Список постов</Link>
          <Link to="/add">Добавить пост</Link>
        </nav>
        <Routes>
          <Route path="/" element={<PostList posts={posts} deletePost={deletePost} />} />
          <Route path="/add" element={<PostForm addPost={createPost} />} />
          <Route path="/post/:id" element={<PostDetail posts={posts} />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
