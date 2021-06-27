import React from 'react';
import Fetch from './Fetch';

const ProductList = (props) => {
    return <Fetch url={'http://localhost:8000/api/product/list'}>
        <ProductListInner {...props} />
    </Fetch>
}

const ProductListInner = ({data}) => {
    console.log(data);
    return <ul>
        {data.map(p => <li key={p.id}>{p.name}</li>)}
    </ul>
}

export default ProductList;
