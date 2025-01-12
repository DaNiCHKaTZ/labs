/* eslint-disable no-unused-vars */
/* eslint-disable react/prop-types */
import React, { Component, createRef } from 'react';
import { nanoid } from 'nanoid';
import Todo from './components/Todo';
import Form from './components/Form';
import FilterButton from './components/FilterButton';

const FILTER_MAP = {
  All: () => true,
  Active: task => !task.completed,
  Completed: task => task.completed,
};
const FILTER_NAMES = Object.keys(FILTER_MAP);

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tasks: props.tasks,
      filter: 'All'
    };

    this.listHeadingRef = createRef();
    this.addTask = this.addTask.bind(this);
    this.editTask = this.editTask.bind(this);
    this.toggleTaskCompleted = this.toggleTaskCompleted.bind(this);
    this.deleteTask = this.deleteTask.bind(this);
    this.setFilter = this.setFilter.bind(this);
  }

  addTask(name) {
    const newTask = { id: `todo-${nanoid()}`, name, completed: false };
    this.setState({
      tasks: [...this.state.tasks, newTask]
    });
  }

  editTask(id, newName) {
    const editedTaskList = this.state.tasks.map(task => {
      if (id === task.id) {
        return { ...task, name: newName };
      }
      return task;
    });
    this.setState({ tasks: editedTaskList });
  }

  toggleTaskCompleted(id) {
    const updatedTasks = this.state.tasks.map(task => {
      if (id === task.id) {
        return { ...task, completed: !task.completed };
      }
      return task;
    });
    this.setState({ tasks: updatedTasks });
  }

  deleteTask(id) {
    const remainingTasks = this.state.tasks.filter(task => id !== task.id);
    this.setState({ tasks: remainingTasks });
  }

  setFilter(filter) {
    this.setState({ filter });
  }

  componentDidUpdate(prevProps, prevState) {
    if (prevState.tasks.length > this.state.tasks.length) {
      this.listHeadingRef.current.focus();
    }
  }

  render() {
    const { tasks, filter } = this.state;
    const taskList = tasks
      .filter(FILTER_MAP[filter])
      .map(task => (
        <Todo
          id={task.id}
          name={task.name}
          completed={task.completed}
          key={task.id}
          toggleTaskCompleted={this.toggleTaskCompleted}
          deleteTask={this.deleteTask}
          editTask={this.editTask}
        />
      ));

    const filterList = FILTER_NAMES.map(name => (
      <FilterButton
        key={name}
        name={name}
        isPressed={name === filter}
        setFilter={this.setFilter}
      />
    ));

    const tasksNoun = taskList.length !== 1 ? 'tasks' : 'task';
    const headingText = `${taskList.length} ${tasksNoun} remaining`;

    return (
      <div className="todoapp stack-large">
        <h1>TodoMatic</h1>
        <Form addTask={this.addTask} />
        <div className="filters btn-group stack-exception">
          {filterList}
        </div>
        <h2 id="list-heading" tabIndex="-1" ref={this.listHeadingRef}>
          {headingText}
        </h2>
        <ul
          role="list"
          className="todo-list stack-large stack-exception"
          aria-labelledby="list-heading"
        >
          {taskList}
        </ul>
      </div>
    );
  }
}

export default App;
