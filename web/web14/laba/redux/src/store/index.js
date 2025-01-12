import { createStore } from 'redux';
import postReducer from '../reducers/PostReducers.js';


const store = createStore(postReducer);

export default store;
