import React, { Component } from "react";
import "./App.css";
import PuzzleList from "./PuzzleList.js";
import PuzzleDisplay from "./PuzzleDisplay.js";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      display_puzzle: {
        title: "",
        question: ""
      }
    };
  }

  handleClick(puz) {
    this.setState({
      display_puzzle: puz
    });
  }

  render() {
    return (
      <div className="App">
        <PuzzleList
          className="PuzzleList"
          handleClick={this.handleClick.bind(this)}
        />
        <PuzzleDisplay
          className="PuzzleDisplay"
          title={this.state.display_puzzle.title}
          question={this.state.display_puzzle.question}
        />
      </div>
    );
  }
}

export default App;
