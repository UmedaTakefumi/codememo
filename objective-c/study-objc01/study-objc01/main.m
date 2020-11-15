//
//  main.m
//  study-objc01
//
//  Created by UmedaTakefumi on 2020/11/14.
//

#import <Foundation/Foundation.h>

#define FOOA 0
#define RESTAPI_URL @"https://api.example.co.jp/"
# define fuga(a, b, c, d, e) a + b + c + d + e

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
    
    NSLog(@"%d", FOOA);
    NSLog(@"%@", RESTAPI_URL);
    NSLog(@"%d", fuga(1, 2, 3, 4, 5));
    
    
    // ref:
    //      https://sodocumentation.net/ja/objective-c/topic/1461/列挙型
    typedef enum {
        NUM_A = 1,
        NUM_B = 2,
        NUM_C = 3,
        NUM_D = 4,
        NUM_E = 5,
        NUM_F = 6,
        NUM_G = 7,
        
    } NUMBER_PART;
    
    NUMBER_PART SUUJI_01 = NUM_A;
    NUMBER_PART SUUJI_02 = NUM_B;
    
    NSLog(@"+-------------------------------------+");
    NSLog(@"%d", SUUJI_01);
    NSLog(@"+-------------------------------------+");
    NSLog(@"%d", SUUJI_02);
    NSLog(@"+-------------------------------------+");

    return 0;
}
