import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import { deletePost } from '../actions/PostAction.js';

function PostList() {
  const posts = useSelector((state) => state.posts);
  const dispatch = useDispatch();

  return (
    <div>
      {posts.map((post, index) => (
        <div key={index} className="post">
          <Link to={`/post/${index}`}>
            <h2>{post.title}</h2>
          </Link>
          <p>{post.content}</p>
          <span>{post.date}</span>
          <button onClick={() => dispatch(deletePost(index))}>Удалить</button>
        </div>
      ))}
    </div>
  );
}

export default PostList;
