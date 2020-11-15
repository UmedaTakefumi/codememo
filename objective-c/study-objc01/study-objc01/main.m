//
//  main.m
//  study-objc01
//
//  Created by UmedaTakefumi on 2020/11/14.
//

#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        // insert code here...
        NSLog(@"Hello, World!");
        int foo;
        foo = 0;
        NSLog(@"%d", foo);
    
        int x = 0, y = 1024, z;
        z = 11;
        NSLog(@"%d, %d, %d ", x, y, z);
        
        NSString *foobar = @"hogehoge";
        NSLog(@"%@", foobar);
        
        const int level = 0;
        NSLog(@"%d", level);
        
    }
    
    return 0;
}
