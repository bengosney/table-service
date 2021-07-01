import React from "react";
import Fetch from "./Fetch";
import ProductListFetch from "./productList";

import { Box, Tab, Tabs } from "grommet";

export const CategoryListFetch = props => {
  return (
    <Fetch url={"/product/category/list"}>
      <CategoryList {...props} />
    </Fetch>
  );
};

export const CategoryList = ({ data }) => {
  return (
    <Tabs>
      {data.map(p => (
        <Tab key={p.id} title={p.name}>
          <ProductListFetch category={p.id} />
        </Tab>
      ))}
    </Tabs>
  );
};

export default CategoryListFetch;
