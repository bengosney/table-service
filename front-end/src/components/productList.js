import React from "react";
import Fetch from "./Fetch";

import {
  DocumentCard,
  DocumentCardActions,
  DocumentCardActivity,
  DocumentCardLocation,
  DocumentCardPreview,
  DocumentCardTitle,
  IDocumentCardPreviewProps,
} from '@fluentui/react/lib/DocumentCard';

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

const documentCardActions = [
  {
    iconProps: { iconName: 'Share' },
    onClick: console.log('share'),
    ariaLabel: 'share action',
  },
  {
    iconProps: { iconName: 'Pin' },
    onClick: console.log( 'pin'),
    ariaLabel: 'pin action',
  },
  {
    iconProps: { iconName: 'Ringer' },
    onClick: console.log('notifications'),
    ariaLabel: 'notifications action',
  },
];

export const ProductList = ({ data }) => {
  return (
    <div>
      {data.map(p => (
        <DocumentCard key={p.id}>
          <DocumentCardTitle title={p.name} />
          <DocumentCardActions actions={documentCardActions} views={432} />
        </DocumentCard>
      ))}
    </div>
  );
};

export const ProductListy = ({ data }) => {
  return (
    <ul>
      {data.map(p => (
        <li key={p.id}>
          {p.name}
        </li>
      ))}
    </ul>
  );
};

export default ProductListFetch;
