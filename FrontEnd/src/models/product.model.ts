import { BaseModel } from ".";
import { ProductCategory } from "./product-category.model";

export interface Product extends BaseModel {
  name: string;
  state: "in" | "os";
  categories?: ProductCategory[];
  pictures?: string[];
}

export interface SearchedProduct extends Omit<Product, "pictures"> {
  name: string;
  state: "in" | "os";
  categories?: ProductCategory[];
  picture?: string;
}
