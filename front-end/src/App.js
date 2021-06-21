import Form from "@rjsf/fluent-ui";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import useGroupedSchemas from "./hooks/useGroupedSchemas";
import useSettings from "./hooks/useSettings";
import Nav from "./components/nav";
import Admin from "./components/admin";
import { ucfirst } from "./utils";

import "./App.css";

function App() {
  const settings = useSettings();
  const grouped_schemas = useGroupedSchemas(settings.apiURL);

  const navItems = Object.keys(grouped_schemas)
    .filter(key => key.toLowerCase() != "order")
    .map(key => {
      const url = `/admin/${key.toLowerCase()}`;
      return {
        name: ucfirst(key),
        url: url
      };
    });

  const nav = [
    {
      links: [
        {
          name: "Home",
          url: "/"
        },
        {
          name: "Orders",
          url: "/orders/"
        },
        {
          name: "Admin",
          url: "/admin/",
          links: navItems
        }
      ]
    }
  ];
  const schemas = {};

  return (
    <div className="App">
      <div className={"ms-Grid"}>
        <div className={"ms-Grid-row "}>
          <Router>
            <div className={"ms-Grid-col ms-md4"}>
              <Nav groups={nav} />
            </div>
            <div className={"ms-Grid-col ms-md6"}>
              <Switch>
                <Route path="/" exact>
                  <h1>Home</h1>
                </Route>
                <Route path="/orders/">
                  <h1>Orders</h1>
                </Route>
                <Route path="/admin/">
                  <Admin />
                </Route>
              </Switch>
            </div>
          </Router>
        </div>
      </div>
    </div>
  );
}

export default App;
