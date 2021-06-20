import { useEffect, useState } from "react";
import Form from "@rjsf/fluent-ui";
import {
  Nav,
  INavLink,
  INavStyles,
  INavLinkGroup,
} from "@fluentui/react/lib/Nav";
import { useHistory } from "react-router-dom";

import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import useGroupedSchemas from "./hooks/useGroupedSchemas";
import useSettings from "./hooks/useSettings";

import "./App.css";

const L = (props) => {
  console.log(props);
};

function App() {
  const history = useHistory();
  const settings = useSettings();
  const grouped_schemas = useGroupedSchemas(settings.apiURL);

  const navItems = Object.keys(grouped_schemas).map((key) => {
    const url = `/orm/${key.toLowerCase()}`;
    return {
      name: key,
      url: url,
      onClick: (e) => {
        e.preventDefault();
        history.push(url);
      },
    };
  });

  const nav = [
    {
      links: [
        {
          name: "Home",
          url: "/",
          onclick: (e) => {
            e.preventDefault();
            history.push("/");
          },
        },
        {
          name: "ORM",
          links: navItems,
        },
      ],
    },
  ];
  const schemas = {};

  return (
    <div className="App">
      <Router>
        <div>
          <Nav groups={nav} />
        </div>
        <div>
          {Object.keys(schemas).map((k) => (
            <div key={k}>
              <p>{k}</p>
              <Form schema={schemas[k]} />
              <hr />
            </div>
          ))}
        </div>
        <Switch>
          <Route path="/">
            <h1>Home</h1>
          </Route>
          <Route path="/orm">
            <h1>ORM</h1>
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
