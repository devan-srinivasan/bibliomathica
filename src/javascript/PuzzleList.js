import React, { Component } from "react";
import Puzzle from "./Puzzle.js";
import "./react-stylesheets/PuzzleList.css";
import web_config from "./config.js";

class PuzzleList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      puzzles: []
    };
  }

  handleClick(puz) {
    this.props.handleClick(this.state.puzzles[puz.index]);
  }

  getPuzzles() {
    if (web_config.mode == "dev") {
      host_address = web_config.dev.address + ":" + web_config.dev.port;
    } else {
      host_address = web_config.prod.address;
    }

    fetch(host_address + "/get_all_puzzles/", {
      method: "GET"
    })
      .then(function (response) {
        return response.json();
      })
      .then((data) => {
        this.setState({ puzzles: data });
      });
  }

  render() {
    const puzzleItems = this.state.puzzles.map((puz, index) => (
      <Puzzle
        className="Puzzle"
        key={index}
        title={puz.title}
        index={index}
        handleClick={this.handleClick.bind(this)}
      />
    ));
    return (
      <div className="PuzzleList">
        <div className="list-header">
          <h2>Puzzles</h2>
          <button className="btn btn-secondary" onClick={() => this.getPuzzles()}>Refresh</button>
        </div>
        {puzzleItems}
      </div>
    );
  }
}

export default PuzzleList;
