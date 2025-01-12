import React from 'react';

function PostList({ posts, deletePost }) {
  return (
    <div>
      {posts.map((post, index) => (
        <div key={index} className="post">
          <h2>{post.title}</h2>
          <p>{post.content}</p>
          <span>{post.date}</span>
          <button onClick={() => deletePost(index)}>Удалить</button>
        </div>
      ))}
    </div>
  );
}

export default PostList;
