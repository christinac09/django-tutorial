export function shuffle<T>(array: T[]): T[] {
  for (let i = array.length - 1; i >= 1; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[array[i], array[j]] = [array[j]!, array[i]!]   //! tells ts it's not undefined
  }
  return array
}
/** Makes a request to an endpoint \
 * @param endpoint - 
 * @param method - 
 * @param body - 
 */
export async function requestEndpoint(endpoint: string, method?: string, body?: object): Promise<void>;

export async function fetchEndpoint(url: string, method?: string, body?: object){
  const config = useRuntimeConfig();
  const token = await $fetch(config.public.apiBase + url, {
    method: method,
    body: body,
  });
  return token
}
  
