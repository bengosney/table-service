import React from "react";
import Fetch from "./Fetch";

export const ProductListFetch = ({ category = null, ...props }) => {
  const url =
    category === null
      ? "/product/list"
      : `/product/category/${category}/products`;

  return (
    <Fetch url={url}>
      <ProductList {...props} />
    </Fetch>
  );
};

export const ProductList = ({ data }) => {
  console.log(data);
  return (
    <ul>
      {data.map(p => (
        <li key={p.id}>{p.name}</li>
      ))}
    </ul>
  );
};

export default ProductListFetch;
