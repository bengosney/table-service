import React from "react";
import Fetch from "./Fetch";
import { Box, Card, CardBody, CardHeader, CardFooter, Button } from "grommet";

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
  return (
    <Box>
      {data.map(p => (
        <Card pad={"medium"}>
          <CardHeader>{p.name}</CardHeader>
          <CardBody>Description</CardBody>
          <CardFooter>£0.00 <Button>Add to order</Button></CardFooter>
        </Card>
      ))}
    </Box>
  );
};

export default ProductListFetch;
