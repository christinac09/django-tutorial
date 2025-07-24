export function shuffle<T>(array: T[]): T[] {
  for (let i = array.length - 1; i >= 1; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[array[i], array[j]] = [array[j]!, array[i]!]   //! tells ts it's not undefined
  }
  return array
}
/** Makes a request to an endpoint \ shows up when calling the function
 * @param endpoint - The endpoint to request, relative to the API base URL.
 * @param method - The HTTP method to use (GET, POST, etc.). Defautls to GET.
 * @param body - The body of the request, if applicable. Defaults to undefined (if GET)
 */
export async function requestEndpoint(endpoint: string, method?: string, body?: object): Promise<void>;   // ? makes it optional; this function thing is called an overload(?)

/** Makes a request to an endpoint \
 * @template T - The expected response type. 
 * @param endpoint - The endpoint to request, relative to the API base URL.
 * @param method - The HTTP method to use (GET, POST, etc.). Defautls to GET.
 * @param body - The body of the request, if applicable. Defaults to undefined.
*/
export async function requestEndpoint<T>(endpoint: string, method?:string, body?:object): Promise<T>;

export async function requestEndpoint<T>(endpoint: string, method?: string, body?: object): Promise<T|void>{
  const config = useRuntimeConfig();

  const options: RequestInit = method ? {
    method: method, 
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body),
  } : {};

  const res = await fetch(`${config.public.apiBase}${endpoint}`, options)
  if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`)

  return res.json() as T;
}
  
