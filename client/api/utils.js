export function isApiError(data) {
  return (
    typeof data === 'object' &&
    data !== null &&
    'type' in data &&
    'fallback_message' &&
    'detail' in data
  )
}
