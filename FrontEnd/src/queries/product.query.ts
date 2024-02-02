import { AxiosError, AxiosResponse } from "axios";
import { api } from "../axios";
import { useQuery } from "react-query";
import { Product, SearchedProduct } from "../models/product.model";

export function useGetProducts(search?: string) {
  const { data, isLoading, error, refetch } = useQuery<
    AxiosResponse<(Product | SearchedProduct)[]>,
    AxiosError
  >(["products"], () =>
    api.get("products/", search ? { params: { search } } : undefined)
  );

  return {
    products: data?.data,
    getProductsError: error?.response?.data,
    isGettingProducts: isLoading,
    refetchProducts: refetch,
  };
}
