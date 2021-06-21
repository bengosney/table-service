import { Nav as FluentNav } from "@fluentui/react/lib/Nav";

import { useHistory } from "react-router-dom";

const Nav = ({ ...props }) => {
  const history = useHistory();

  return <FluentNav {...props} onLinkClick={(event, item) => {
      event.preventDefault();
      if (item && item.url) {
          history.push(item.url);
      }
  }}
  selectedKey={history.location.pathname}
  />;
};

export default Nav;
