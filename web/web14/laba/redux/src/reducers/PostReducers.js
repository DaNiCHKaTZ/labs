import { CREATE_POST, DELETE_POST } from '../actions/PostAction.js';

const initialState = {
  posts: []
};

const postReducer = (state = initialState, action) => {
  switch (action.type) {
    case CREATE_POST:
      return {
        ...state,
        posts: [...state.posts, action.payload]
      };
    case DELETE_POST:
      return {
        ...state,
        posts: state.posts.filter((_, i) => i !== action.payload)
      };
    default:
      return state;
  }
};

export default postReducer;
