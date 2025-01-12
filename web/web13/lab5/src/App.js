import React, { useState } from 'react';
import PostForm from './components/PostForm';
import PostList from './components/PostList';
import './App.css';

function App() {
  const [posts, setPosts] = useState([]);

  const addPost = (title, content) => {
    const newPost = {
      title,
      content,
      date: new Date().toLocaleString()
    };
    setPosts([...posts, newPost]);
  };

  const deletePost = (index) => {
    const updatedPosts = posts.filter((_, i) => i !== index);
    setPosts(updatedPosts);
  };

  return (
    <div className="App">
      <h1>Посты</h1>
      <PostForm addPost={addPost} />
      <PostList posts={posts} deletePost={deletePost} />
    </div>
  );
}

export default App;
