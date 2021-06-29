import React from 'react';
import Fetch from './Fetch';
import ProductListFetch from './productList';


export const CategoryListFetch = (props) => {
    return <Fetch url={'/product/category/list'}>
        <CategoryList {...props} />
    </Fetch>
}

export const CategoryList = ({data}) => {
    return <ul>
        {data.map(p => <li key={p.id}>{p.name}
        <ProductListFetch category={p.id} />
        </li>)}
    </ul>
}

export default CategoryListFetch;
