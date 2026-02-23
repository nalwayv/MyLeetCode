function hasAllCodes(s: string, k: number): boolean {
    var maxSize = 1 << k;
    const seen = new Set<string>();
    
    for(var i = 0; i <= s.length - k; i++) {
        seen.add(s.slice(i, i+k));
        if (seen.size == maxSize) {
            return true;
        }
    }

    return false;
};